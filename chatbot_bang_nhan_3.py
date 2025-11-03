import random
import re
from typing import Optional


def chao_hoi() -> None:
    print("Xin chào! Mình là Trợ giảng Bảng nhân 3.")
    print("Bạn có thể gõ 'thoát' bất cứ lúc nào để kết thúc cuộc trò chuyện.")
    print("Nào, chúng ta cùng ôn bảng nhân 3 nhé!\n")


def chon_cau_hoi() -> tuple[str, int, int]:
    loai = random.choice(["phep_nhan", "tim_phep_tinh"])
    so = random.randint(0, 10)
    dap_an = 3 * so

    if loai == "phep_nhan":
        cau_hoi = f"3 nhân với {so} bằng bao nhiêu?"
    else:
        cau_hoi = f"Trong bảng nhân 3, phép tính nào cho ra kết quả {dap_an}?"

    return cau_hoi, so, dap_an


def la_lenh_thoat(tra_loi: str) -> bool:
    return tra_loi.strip().lower() in {"thoat", "thoát", "exit", "quit"}


def kiem_tra_phep_nhan(tra_loi: str, dap_an: int) -> bool:
    try:
        return int(tra_loi.strip()) == dap_an
    except ValueError:
        return False


def tim_so_trong_chuoi(tra_loi: str) -> Optional[int]:
    so_tim_duoc = re.findall(r"\d+", tra_loi)
    if not so_tim_duoc:
        return None
    return int(so_tim_duoc[-1])


def kiem_tra_tim_phep_tinh(tra_loi: str, so: int) -> bool:
    tra_loi_thuong = tra_loi.strip().lower()
    mau_sac = [
        f"3 x {so}",
        f"3 * {so}",
        f"3 nhân {so}",
        f"{so} x 3",
        f"{so} * 3",
        f"{so} nhân 3",
        f"3 nhân với {so}",
        f"{so} nhân với 3",
    ]
    if tra_loi_thuong in {m.lower() for m in mau_sac}:
        return True

    so_tra_loi = tim_so_trong_chuoi(tra_loi_thuong)
    return so_tra_loi == so


def phan_hoi_dung(loai: str, so: int, dap_an: int) -> None:
    if loai == "phep_nhan":
        print("Chính xác! 3 x", so, "=", dap_an)
    else:
        print(f"Đúng rồi! 3 x {so} = {dap_an}.")


def phan_hoi_sai(loai: str, so: int, dap_an: int) -> None:
    if loai == "phep_nhan":
        print(f"Chưa đúng. 3 x {so} = {dap_an}. Cùng thử câu khác nhé!")
    else:
        print(
            f"Chưa chính xác. Kết quả {dap_an} đến từ phép tính 3 x {so}."
            " Hãy chú ý hơn nhé!"
        )


def choi() -> None:
    chao_hoi()
    while True:
        cau_hoi, so, dap_an = chon_cau_hoi()
        print("Bot:", cau_hoi)
        tra_loi = input("Bạn: ")

        if la_lenh_thoat(tra_loi):
            print("Tạm biệt! Hẹn gặp lại bạn để luyện tập bảng nhân 3 lần sau nhé!")
            break

        if "kết quả" in cau_hoi:
            dung = kiem_tra_tim_phep_tinh(tra_loi, so)
            loai = "tim_phep_tinh"
        else:
            dung = kiem_tra_phep_nhan(tra_loi, dap_an)
            loai = "phep_nhan"

        if dung:
            phan_hoi_dung(loai, so, dap_an)
        else:
            phan_hoi_sai(loai, so, dap_an)

        print()


if __name__ == "__main__":
    try:
        choi()
    except KeyboardInterrupt:
        print("\nTạm biệt! Chúc bạn học tốt bảng nhân 3!")
