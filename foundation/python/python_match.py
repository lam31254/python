'''cấu trúc câu lệnh match:
{
   -sử dụng khi: +) khi có các mẫu số tương ứng và rõ ràng
     +) đặc điểm của match là tương ứng với 1 case thì chỉ sử dụng 
     1 giá trị tương ứng và khi tìm đc giá trị tương ứng thì tự out khỏi lệnh
     +)điểm khác nhau giữa if và else là: khi sử dụng thì if và else cho
     các logic phức tạp hơn nhưng với match thì chỉ là 1 case và chỉ 1 giá trị
     +) không cần sử dụng câu lệnh break 
     +) khi tìm được cái đúng theo các case tự out luôn khỏi match
  - các cách sử dụng của match:
     +)Default Value(Sử dụng là dấu (case_:)):
        sử dụng ký hiệu "_" vào cái case cuối cùng của bạn nếu bạn muốn
         code match vẫn được thực thi khi không có cái case nào phù hợp với cái match bạn đưa ra.
         day = 4
        match day:
        case 6:
            print("Today is Saturday")
        case 7:
            print("Today is Sunday")
        case _:
            print("Looking forward to the Weekend")
     +)Combine Values(câu lệnh kết hợp nhiều case với cùng 1 giá trị):
        nếu câu lệnh match của bạn với 1 giá trị ứng với nhiều case thì bạn
        có thể kết hợp các case lại với cùng 1 giá trị
        day = 4
        match day:
        case 1 | 2 | 3 | 4 | 5:
            print("Today is a weekday")
        case 6 | 7:
            print("I love weekends!")
     +)If Statements as Guards(sử dụng thêm câu lệnh if để double check giá trị):
        bạn có thể add thêm câu lệnh if để kiểm tra và đưa ra giá trị cho case tương ứng đó:
        month = 5
        day = 4
        match day:
        case 1 | 2 | 3 | 4 | 5 if month == 4:
            print("A weekday in April")
        case 1 | 2 | 3 | 4 | 5 if month == 5:
            print("A weekday in May")
        case _:
            print("No match")
 }
'''
a=input("hộp số tương ứng khi chạy: ")
print(type(a))
match a:
    case "1":
        print("tốc độ chạy tối đa của bạn là từ 0 km/h ~ 10km/m")
    case "2":
        print("tốc độ chạy tối đa của bạn là từ 10 km/h ~ 20km/m")
    case "3":
        print("tốc độ chạy tối đa của bạn là từ 30 km/h ~ 40km/m")
    case "4":
        print("tốc độ chạy tối đa của bạn là từ 40 km/h ~ 50km/m")
    case "5":
        print("tốc độ chạy tối đa của bạn là từ 100km/m")
    case "0":
        print(" bạn đang ở vị trí mor")
    case _:
        print("đang gặp lỗi tại hộp số")
'''
Hãy viết một chương trình Python mô phỏng máy bán vé tự động. Máy có ba loại vé: vé người lớn (adult) giá 50.000 đồng, vé học sinh/sinh viên (student) giá 30.000 đồng 
và vé trẻ em (child) giá 20.000 đồng. Hãy lưu tên và giá vé trong một dictionary.
Chương trình yêu cầu người dùng nhập loại vé, tuổi và phương thức thanh toán. 
Máy chấp nhận ba phương thức là tiền mặt (cash), thẻ (card) và mã QR (qr); hãy lưu chúng trong một set. 
nếu tất cả thông tin hợp lệ, chương trình hiển thị loại vé, tuổi người mua, giá vé, phương thức thanh toán và trạng thái giao dịch. 
Nếu có thông tin không hợp lệ, chương trình phải thông báo nguyên nhân và không xác nhận giao dịch thành công.
'''
