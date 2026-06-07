teams_list = []
match_schedule = []

def generate_combinations_two(lst):
    return [(lst[i], partner) for i in range(len(lst)) for partner in lst[i + 1:]]

def input_teams():
    print("\n--- NHẬP DANH SÁCH ---")
    raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ").strip()
    
    if not raw_input:
        print("Cảnh báo: Danh sách nhập vào trống!")
        return []
    
    raw_teams = [team.strip().upper() for team in raw_input.split(",")]
    local_teams = []
    for team in raw_teams:
        if team and team not in local_teams:
            local_teams.append(team)
            
    print(f"Đã ghi nhận {len(local_teams)} đội: {local_teams}")
    return local_teams

def create_match_schedule(teams_list):
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return []
    
    pairs = generate_combinations_two(teams_list)
    schedule_result = [f"{team_a} vs {team_b}" for team_a, team_b in pairs]

    for index, match in enumerate(schedule_result, start = 1):
        print(f"{index}. {match}")
    print(f"Tổng số trận đấu: {len(schedule_result)} trận.")
    return schedule_result

def generate_match_ids(match_schedule):
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return
    
    for index, match in enumerate(match_schedule, start = 1):
        team_a, team_b = match.split(" vs ")
        
        sub_a = team_a[0:3]
        sub_b = team_b[0:3]

        match_id = f"M{index:02d}-{sub_a:X<3}-{sub_b:X<3}"
        print(f"Trận {index} ({match}) -> ID: {match_id}")

def main():
    global teams_list, match_schedule
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            teams_list = input_teams()
            match_schedule = []
        elif choice == "2":
            match_schedule = create_match_schedule(teams_list)
        elif choice == "3":
            generate_match_ids(match_schedule)
        elif choice == "4":
            print("\nĐã đóng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4!")

if __name__ == "__main__":
    main()