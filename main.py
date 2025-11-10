while True:
    sensor_value = pin0.read_analog()          # Read from rotary angle sensor
    frequency = int((sensor_value / 1023) * 1800 + 200)  # Map to 200–2000 Hz range

    # Play tone continuously while adjusting pitch
    music.pitch(frequency, duration=-1, pin=pin1)  # Continuous tone

    # Small pause for smooth pitch change
    sleep(20)
