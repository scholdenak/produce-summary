def produce_daily_summary(file, day):
    """Puts melon delivery info from file into daily report""" 

    print(day)
    #prints day of report
    the_file = open(file)
    #opens file for use in function
    for line in the_file:
    #iterates over file to separate lines
        line = line.rstrip()
        #removes extra characters at end of lines
        words = line.split('|')
        #splits the lines of string for data variable assignment

        melon = words[0]
        count = words[1]
        amount = words[2]
        #assigns valiables to words at specified index

        print(f"Delivered  {count} {melon}s for total of ${amount}.")
        #prints "f" string with variables printed in
    
    the_file.close()
    #closes file

produce_daily_summary("um-deliveries-20140519.txt", "Day 1")
#calls function on text report on specified date

# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
