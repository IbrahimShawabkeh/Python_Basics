position = 0
const_velocity = 2
time_step = 1

print ("positions for each step:")
for frame in range(5):
	position += const_velocity * time_step
	print ("Frame", frame + 1, "new position is", position, "meters")
print ("All positions listing for each point complete!")
