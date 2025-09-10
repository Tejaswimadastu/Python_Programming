day1 = ["Alice@example.com", "bob@example.com", "ALICE@example.com", "carol@example.com"]
day2 = ["bob@example.com", "dave@example.com", "Eve@example.com", "alice@example.com"]
day3 = ["alice@example.com", "eve@example.com", "frank@example.com", "bob@example.com"]

day1_set = set(email.lower() for email in day1)
day2_set = set(email.lower() for email in day2)
day3_set = set(email.lower() for email in day3)

all_attendees = day1_set | day2_set | day3_set
all_three_days = day1_set & day2_set & day3_set
exactly_one_day = (day1_set - day2_set - day3_set) | (day2_set - day1_set - day3_set) | (day3_set - day1_set - day2_set)

day1_day2_overlap = day1_set & day2_set
day2_day3_overlap = day2_set & day3_set
day1_day3_overlap = day1_set & day3_set

print("==== Tech Workshop Attendee Report ====")
print(f"Total unique attendees: {len(all_attendees)}")
print(f"List of all unique attendees: {sorted(all_attendees)}\n")
print(f"Attendees who attended all three days ({len(all_three_days)}): {sorted(all_three_days)}\n")
print(f"Attendees who attended exactly one day ({len(exactly_one_day)}): {sorted(exactly_one_day)}\n")
print(f"Pairwise overlaps:")
print(f"  Day1 & Day2 ({len(day1_day2_overlap)}): {sorted(day1_day2_overlap)}")
print(f"  Day2 & Day3 ({len(day2_day3_overlap)}): {sorted(day2_day3_overlap)}")
print(f"  Day1 & Day3 ({len(day1_day3_overlap)}): {sorted(day1_day3_overlap)}")
