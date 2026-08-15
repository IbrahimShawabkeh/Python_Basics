height = 10
velocity = 0
gravity = 9.81
time_step = 0.01

print ("Tracking Falling object's location and velocity initialized!")
while height > 0:
	velocity += gravity * time_step
	height -= velocity * time_step
	if height > 0:
		print (f"height: {height:.4}, velocity: {velocity:.4} m/s")
print ("Impact event!! target reached ground!")
