
import csv
while True:
  def get_stat_info(Pname):
      with open('getBatterStats.csv', 'r', newline='', encoding='utf-8') as file:
          reader = csv.reader(file)
          next(reader)  # Skip the header row if it exists
          for row in reader:
              if row[1] == Pname:
                  print("RANK:", row[0])
                  print("YRS:", row[2])
                  print("G:", row[3])
                  print("AB:", row[4])
                  print("R:", row[5])
                  print("H:", row[6])
                  print("2B:", row[7])
                  print("3B:", row[8])
                  print("HR:", row[9])
                  print("RBI:", row[10])
                  print("BB:", row[11])
                  print("SO:", row[12])
                  print("SB:", row[13])
                  print("CS:", row[14])
                  print("BA:", row[15])                  
                  return
          print("Airport not found.")
  
  # Example usage
  playerName = input("ENTER PLAYER NAME: ")
  get_stat_info(playerName)

