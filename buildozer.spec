[app]
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir = .
version = 0.1
requirements = python3,kivy

# Используем системный SDK
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# Версии
android.api = 31
android.minapi = 21
android.sdk = 34
android.build_tools_version = 34.0.0

[buildozer]
log_level = 2
