from datetime import datetime

if __name__ == "__main__":
    currentTime = '2023-08-28T04:03:00'
    currentTime = datetime.strftime(currentTime, "%Y-%M-%D%T")
    convertedTime = datetime.strptime(currentTime, "%B %d %Y")
    print(convertedTime)
