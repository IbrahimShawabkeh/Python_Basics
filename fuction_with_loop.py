def	update_position(position, velocity, time):
	while position <= 20:
		position += velocity * time
		print ("Position update: ", position)
update_position(0, 5, 0.1)
