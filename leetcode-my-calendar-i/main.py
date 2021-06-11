class MyCalendar:

    def __init__(self):
        self.list_book = []

    def book(self, start: int, end: int) -> bool:
        if not self.list_book:
            self.list_book.append([start, end])
            return True
        
        possible = True
        for booking in self.list_book:
            if booking[0] <= start < booking[1] or booking[0] < end <= booking[1] or (start <= booking[0] and end >= booking[1]):
                possible = False
        
        if possible:
            self.list_book.append([start, end])
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
def main():
    obj = MyCalendar()
    list_test = [#[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]
                 [97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]
                ]
    
    for test in list_test:
        print(obj.book(test[0], test[1]), " = ", test, obj.list_book)
if __name__ == "__main__":
    main()




# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.