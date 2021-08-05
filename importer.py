import bs4

html = bs4.BeautifulSoup(open("data.html"), "html.parser")
rows = html.find_all("tr")


def process_location(location, start, end):
    if "?" in start or "?" in end:
        return
    if not start.count(".") == 2 and end.count(".") == 2:
        return
    location = location.split("\n")[0]
    start = [s.lstrip("0") for s in start.split(".")]
    end = [e.lstrip("0") for e in end.split(".")]
    print(
        f'"{location}": (({start[0]}, {start[1]}, {start[2]}), ({end[0]}, {end[1]}, {end[2]}))'
    )


for row in rows:
    location, start, end = row.find_all("td")
    if "\n" in end.text:
        locations = location.text.split("\n")
        start = start.text.split("\n")
        end = end.text.split("\n")
        date_count = len([s for s in start if s.strip()])
        location_count = len([l for l in locations if l])
        if date_count == location_count:
            for _ in range(date_count):
                process_location(locations[_], start[_], end[_])
        else:
            common = ""
            current = ""
            if not start[0].strip():
                common = f" - {locations[0]}"
                locations = locations[1:]
            for _ in range(date_count):
                if start[_].strip():
                    process_location(current + locations[_] + common, start[_], end[_])
                    current = ""
                else:
                    current = f"{locations[_]} - "
    else:
        process_location(location.text, start.text, end.text)
