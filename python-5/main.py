from datetime import datetime, timedelta

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(records):
    phone_fees = {}

    for record in records:
        if is_one_day_call(record['start'], record['end']):
            previous_fee_amount = get_phone_fee_amount(
                                    record['source'],
                                    phone_fees)

            call_fee = calculate_fee(record['start'], record['end'])
            phone_fees[record['source']] = previous_fee_amount + call_fee

    report = buil_report(phone_fees)

    return report


def get_phone_fee_amount(phone, phone_fees):
    phone_fee_amount = 0

    if phone in phone_fees:
        phone_fee_amount = phone_fees[phone]

    return phone_fee_amount


def is_one_day_call(start_time, end_time):
    start_time_parsed = datetime.fromtimestamp(start_time)
    end_time_parsed = datetime.fromtimestamp(end_time)

    if start_time_parsed.date() == end_time_parsed.date():
        return True

    return False


def is_day_time_minute(time):
    time_parsed = datetime.fromtimestamp(time)

    if (time_parsed.time().hour >= 6 and
            time_parsed.time().hour <= 21):
        return True


def calculate_fee(start_time, end_time):
    start_time_parsed = datetime.fromtimestamp(start_time)
    end_time_parsed = datetime.fromtimestamp(end_time)

    minute_fee = 0
    permanent_fee = 0.36
    total_fee = permanent_fee

    time_count = start_time_parsed

    while time_count <= end_time_parsed:
        minute_fee = 0

        if is_day_time_minute(time_count.timestamp()):
            minute_fee = 0.09

        one_minute = timedelta(seconds=60)

        time_count = time_count + one_minute

        if time_count <= end_time_parsed:
            total_fee = total_fee + minute_fee

    return total_fee


def buil_report(call_fees):
    report = []
    record = {}

    sort_call_fees = sorted(
                        call_fees.items(),
                        key=lambda x: x[1],
                        reverse=True)

    for source, fee in sort_call_fees:
        record = {'source': source, 'total': float((f'{fee:.2f}'))}
        report.append(record)

    return report


classify_by_phone_number(records)
