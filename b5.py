student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


def find_student(records, student_id):
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index
    return -1


def display_statements(records):
    print("\n--- SAO KÊ ĐIỂM SỐ ---")
    for index, student in enumerate(records, start=1):
        points = student["current_points"]

        if points < 500:
            status = "Cần tích lũy thêm"
        elif points <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"

        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Hiện có: {student['current_points']} | "
            f"Đã tiêu: {student['spent_points']} | "
            f"Hoàn trả: {student['refunded_points']} | "
            f"Hệ số: x{student['multiplier']} | "
            f"Trạng thái: {status}"
        )

def redeem_rewards(records):
    student_id = input("Nhập mã học viên đổi quà: ").strip().upper()
    index = find_student(records, student_id)
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    try:
        points = int(input("Nhập số điểm cần tiêu: "))
        if points <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return
        if points > records[index]["current_points"]:
            print("Số dư điểm không đủ để thực hiện giao dịch!")
            return

        records[index]["current_points"] -= points
        records[index]["spent_points"] += points

        print(
            f">> Giao dịch thành công! "
            f"'{records[index]['name']}' đã tiêu {points} điểm. "
            f"Số dư còn lại: "
            f"{records[index]['current_points']} điểm."
        )

    except ValueError:
        print("Vui lòng nhập số nguyên!")


def appeal_score(records):
    student_id = input("Nhập mã học viên cần phúc khảo: ").strip().upper()
    index = find_student(records, student_id)
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    try:
        points = int(input("Nhập số điểm hoàn lại: "))
        if points <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return
        if points > records[index]["spent_points"]:
            print(
                "Không thể hoàn số điểm lớn hơn "
                "tổng điểm đã tiêu!"
            )
            return

        records[index]["spent_points"] -= points
        records[index]["current_points"] += points
        records[index]["refunded_points"] += points

        print(
            f">> Hoàn điểm thành công! "
            f"'{records[index]['name']}' "
            f"được cộng lại {points} điểm."
        )

    except ValueError:
        print("Vui lòng nhập số nguyên!")


def activate_multiplier(records):
    student_id = input("Nhập mã học viên nhận hệ số: ").strip().upper()
    index = find_student(records, student_id)
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    try:
        multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))
        if multiplier < 1.0 or multiplier > 3.0:
            print(
                "Hệ số nhân không hợp lệ. "
                "Chỉ chấp nhận số từ 1.0 đến 3.0"
            )
            return

        records[index]["multiplier"] = multiplier

        print(
            f">> Đã kích hoạt hệ số x{multiplier} "
            f"cho học viên "
            f"'{records[index]['name']}'."
        )

    except ValueError:
        print(
            "Hệ số nhân không hợp lệ. "
            "Chỉ chấp nhận số từ 1.0 đến 3.0"
        )


def grade_assignment(records):
    student_id = input("Nhập mã học viên vừa nộp bài: ").strip().upper()
    index = find_student(records, student_id)
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    try:
        base_points = int(input("Nhập số điểm gốc đạt được: "))
        if base_points <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        multiplier = records[index]["multiplier"]
        earned_points = int(base_points * multiplier)
        records[index]["current_points"] += earned_points

        print(
            f">> Hệ số hiện tại của "
            f"'{records[index]['name']}' "
            f"là x{multiplier}."
        )

        print(
            f">> Điểm thực nhận: "
            f"{earned_points}."
        )

        print(
            f">> Đã cộng {earned_points} điểm "
            f"vào tài khoản!"
        )

    except ValueError:
        print("Vui lòng nhập số nguyên!")


if __name__ == "__main__":
    while True:
        print("""
===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
1. Hiển thị sao kê điểm số
2. Đổi điểm lấy phần thưởng
3. Phúc khảo bài thi (Hoàn điểm)
4. Kích hoạt (Hệ số nhân điểm)
5. Chấm bài (thêm điểm)
6. Thoát chương trình
=====================================================
""")

        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case "1":
                display_statements(student_records)

            case "2":
                redeem_rewards(student_records)

            case "3":
                appeal_score(student_records)

            case "4":
                activate_multiplier(student_records)

            case "5":
                grade_assignment(student_records)

            case "6":
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")