extends Node3D

var udp := PacketPeerUDP.new()
var port := 5005

@onready var waving_player: AnimationPlayer = $Waving/AnimationPlayer


func _ready() -> void:
	print("MAIN.GD IS RUNNING")

	var result = udp.bind(port)

	if result == OK:
		print("UDP connected on port ", port)
	else:
		print("UDP bind failed: ", result)

	print("Animations found:")

	for animation_name in waving_player.get_animation_list():
		print(" - ", animation_name)


func _process(_delta: float) -> void:

	while udp.get_available_packet_count() > 0:

		var packet := udp.get_packet()
		var message := packet.get_string_from_utf8().strip_edges()

		print("SIGN RECEIVED: ", message)

		if message.to_lower() == "hello":

			print("HELLO RECEIVED — PLAYING WAVING")

			waving_player.stop()
			waving_player.play("mixamo_com")
