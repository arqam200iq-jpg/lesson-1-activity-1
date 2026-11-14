"""
1) Ask for agent details.
   a) Ask the user to enter their real name.
   b) Ask the user to enter their favourite gadget.
   c) Store both inputs as text values.
"""
name=input("enter your real name,agent: ")
gadget=input("enter your favourite gadget,agent: ")
"""
2) Store agent information.
   a) Create variables for agent number, speed rating, mission count, height, and active status.
   b) Use different data types such as integer, float, string, and Boolean.
"""
agent_number=7
speed_rating=9.5
mission_count=12
height=1.65
is_active=True
"""
3) Display each value and its data type.
   a) Print the agent name and gadget.
   b) Print number, rating, mission count, height, and active status.
   c) Use `type()` to show the data type of each value.
"""
print("name=",name,"type=",type(name))
print("gadget=",gadget,"type=",type(gadget))
print("agent_number=",agent_number,"type=",type(agent_number))
print("mission_count",mission_count,"type=",type(mission_count))
print("speed_rating",speed_rating,"type=",type(speed_rating))

print("is_active",is_active,"type=",type(is_active))
print("height=",height,"type=",type(height))

"""
4) Convert values into text.
   a) Use `str()` to convert numbers into strings.
   b) Convert the Boolean value into text.
   c) Print the converted values and their new data types.
"""
agent_number_text=str(agent_number)
is_active_text=str(is_active)
print("new type of number and active statuss",type(agent_number_text),type(is_active_text))
"""
5) Create a secret code name.
   a) Use slicing to get the first three letters of the name.
   b) Use negative indexing to get the last letter.
   c) Join both parts to create the code name.

6) Reverse the gadget name.
   a) Use slicing with `[::-1]` to reverse the gadget text.
   b) Print the reversed gadget name.

7) Build the badge message.
   a) Create separate lines for the agent badge.
   b) Use string concatenation to join text and variables.
   c) Use `.upper()` to make important badge text uppercase.

8) Print the secret agent badge.
   a) Print a badge heading.
   b) Print all badge lines one by one.
   c) Print a closing line to complete the badge.
"""