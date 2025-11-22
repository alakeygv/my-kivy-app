[app]
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1
requirements = python3,kivy
# Принудительно указываем версию build-tools
android.build_tools_version = 34.0.0

# И версию SDK
android.sdk = 34
# Добавь эти настройки
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 28

[buildozer]
log_level = 2
