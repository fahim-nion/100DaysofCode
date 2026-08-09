import requests

s = requests.Session()
s.cookies.set(
    "ASP.NET_SessionId",
    "b4wdzfrceeitwnmi5w3i1v3o",
    domain="https://ucam.buft.edu.bd/Security/Login.aspx"
)

r = s.get("https://ucam.buft.edu.bd/Security/Login.aspx")

print(r.status_code)
print(r.url)
print(r.text[:300])