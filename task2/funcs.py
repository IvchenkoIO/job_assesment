import requests  # for making HTTP requests
from django.http import HttpResponse  # for creating HTTP responses


def create_or_update_models(status,guest_fname,guest_sname,guest_email,phone_number,flat_booked,checkin_date,checkout_date,booking_value):
    from .models import Reservations
    from datetime import datetime
    existing_entry = Reservations.objects.filter(
        checkin_date=datetime.strptime(checkin_date, "%Y-%m-%d").date(),
        checkout_date=datetime.strptime(checkout_date, "%Y-%m-%d").date(),
        guest_email=guest_email,
        flat_booked=flat_booked
    ).first()
    if not existing_entry:
        new_instance=Reservations(
            status=status,
            quest_name=guest_fname+" "+guest_sname,
            guest_email=guest_email,
            phone_number=phone_number,
            flat_booked=flat_booked,
            checkin_date=datetime.strptime(checkin_date, "%Y-%m-%d").date(),
            checkout_date=datetime.strptime(checkout_date, "%Y-%m-%d").date(),
            booking_value=booking_value

        )
        new_instance.save()


def parse_xml_data(data):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(data)

    reservations = root.find(".//Reservations")
    for reservation in reservations.findall(".//Reservation"):
        status = reservation.find("StatusID").text

        customer=reservation.find("CustomerInfo")
        guest_fname = customer.find("Name").text
        guest_sname = customer.find("SurName").text
        guest_email = customer.find("Email").text
        phone_number = customer.find("Phone").text

        infos=reservation.find("StayInfos")
        property=infos.find("StayInfo")
        flat_booked = property.find("PropertyID").text
        checkin_date = property.find("DateFrom").text
        checkout_date = property.find("DateTo").text
        price=property.find("Costs")
        booking_value = price.find("RUPrice").text
        create_or_update_models(status,guest_fname,guest_sname,guest_email,phone_number,flat_booked,checkin_date,checkout_date,booking_value)

def send_xml_request(request):
        xml_request = """
        <Pull_ListReservations_RQ>
            <Authentication>
                <UserName>sid@theflexliving.com</UserName>
                <Password>Rentals2023!</Password>
            </Authentication>
            <DateFrom>2000-09-08 14:00:00</DateFrom>
            <DateTo>2023-10-08 14:00:00</DateTo>
        </Pull_ListReservations_RQ>
        """
        api_url = 'http://new.rentalsunited.com/api/handler.ashx'
        try:
            response = requests.get(api_url, data=xml_request, headers={'Content-Type': 'application/xml'})
            if response.status_code == 200:
                response_data = response.text
                parse_xml_data(response_data)
                return True
            else:
                return False

        except requests.exceptions.RequestException as e:
            return False
