import urllib.parse
import webbrowser

print("=========================================")
print("  🚀 MAP INTERACTIVE SYSTEM BOOTING...  ")
print("=========================================")

# Clean input variables without desktop UI components to block it
start = input("Type Starting City (e.g. Bengaluru) and hit Enter: ").strip()
end = input("Type Ending City (e.g. Mumbai) and hit Enter: ").strip()

if start and end:
    src_clean = urllib.parse.quote(start)
    dst_clean = urllib.parse.quote(end)

    url = f"https://google.com{src_clean}&destination={dst_clean}"

    print(f"\n🔗 Attempting to send web handshake signal...")
    print(f"🌍 Generated Target: {url}")

    webbrowser.open(url)
    print("\n✅ Sent! Look behind your PyCharm window for your browser!")
else:
    print("❌ Values cannot be blank.")
