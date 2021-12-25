#kullanıcı adı admin, şifre 123456 yazınca sisteme giriş başarılı, bunların dışında bir şey yazınca kullanıcı adı veya
#şifre hatalı diyerek kullanıcı adı ve şifreyi isteyen bir uygulama geliştiriniz.

demet=("Admin","123456")
while True:
    kullanıcı=input("Kullanıcı adı?").lower()
    şifre=input("Şifre?")
    if kullanıcı=="admin" and şifre =="123456":
        print("Sisteme giriş başarılı")
        break
    else:
        print("Kullanıcı adı veya şifre yanlış")
