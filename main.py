import turtle
import pandas

#importing the dataframe from the file using pandas
states_data = pandas.read_csv("US_states/us-states-game-start/50_states.csv")
# #screen specifications
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.goto(-120,280)
t.write("Write exit in the input when you are out of guesses!")

screen = turtle.Screen()
screen.title("Name_US_states_game")
image = "US_states/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#taking the input from the user
# print(state_input)
# print(states_data.state)
#converting the states dataframe to a list
states = states_data["state"]
# print(states)
state_list = states.to_list()
# print(state_list)

guessed_list = []


while len(guessed_list) < 51:
    state_input = (screen.textinput(title=f"{len(guessed_list)}/50 States Guessed!",prompt="Enter your guess here:")).title()
    
    if state_input == "Exit" :
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-200,292)
        t.write("The states you missed will be shown with red color, remember them for the next time!!")
        missing_list = [] # assuming an empty list which will hold the missing states
        for state in state_list: # for loop that will loop through the missing states and compare them to the orignal list
            if state not in guessed_list: # if statement 
                missed_state = states_data[states_data.state == state]
                t.goto(int(missed_state.x),int(missed_state.y))
                t.color("red")
                t.write(missed_state.state.item())
                missing_list.append(state)
        print(missing_list)
        screen.exitonclick()
        
    
    if state_input in state_list:
        guessed_list.append(state_input)
        print("Correct")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        user_state = states_data[states_data.state == state_input]
        t.goto(int(user_state.x),int(user_state.y))
        t.write(user_state.state.item()) #item grabs the first element only and ignores the other things 
        
    else:
        print("not correct")
#printing the list of all the states that were not guessed by the user





