import pyshorteners

long_url = "https://www.dropbox.com/scl/fo/1eoutgeqp5fx3bqzs22sr/AGIDZ7SAAEEb6lf4ltm9AP4?rlkey=k051o0w0s0u0jiv35ainqnh1i&st=ygybgrfu&dl=0"
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print(short_url)
