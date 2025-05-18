class Countdown:
    def __init__(self, start):
        # Initialize the starting number for countdown
        self.current = start

    def __iter__(self):
        # Return the iterator object itself
        return self
    
    def __next__(self):
        # If current number is less than 0, stop iteration
        if self.current < 0:
            raise StopIteration
        else:
            # Store the current value to return
            value = self.current
            # Decrement current for the next call
            self.current -= 1
            # Return the current countdown number
            return value

# Create a Countdown object starting from 5
c = Countdown(5)

# Iterate over the Countdown object, printing numbers from 5 to 0
for num in c:
    print(num)
