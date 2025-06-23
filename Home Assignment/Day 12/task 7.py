# 7.	File Always Closes
# o	Open a file (use open("sample.txt", "w")) in try.
# o	Write to it, raise an error manually using raise
# o	In finally, close the file and print "File closed".

try:
    file = open("Adi.txt", "w")
    file.write("Aditya Wagh")
    
    # Manually raise an error
    raise Exception("Manually error raised ")

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    file.close()
    print("File closed.")
