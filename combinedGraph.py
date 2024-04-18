# import matplotlib.pyplot as plt
# import os
# import tempGraph
# import humidGraph
# import vocGraph

# def generate_combined_graph():
#     # Generate the temperature, humidity, and VOCs data
#     temp_data = tempGraph.generate_temperature_graph()
#     humid_data = humidGraph.generate_humidity_graph()
#     voc_data = vocGraph.generate_voc_graph()

#     # Create the graph
#     fig, ax = plt.subplots()

#     # Plot the temperature data
#     ax.plot(range(len(temp_data)), temp_data, label='Temperature')

#     # Plot the humidity data
#     ax.plot(range(len(humid_data)), humid_data, label='Humidity')

#     # Plot the VOCs data
#     ax.plot(range(len(voc_data)), voc_data, label='VOCs')

#     # Set the x-axis label
#     ax.set_xlabel('Time')

#     # Set the y-axis labels
#     ax.set_ylabel('Temperature (°C)')
#     ax.set_ylabel('Humidity (%)')
#     ax.set_ylabel('VOCs (ppm)')

#     # Add a legend
#     ax.legend()

#     # Set the title of the graph
#     ax.set_title('Combined Temperature, Humidity, and VOCs')

#     # Save the graph as a PNG image
#     graph_path = os.path.join('static', 'combined_graph.png')
#     fig.savefig(graph_path)

#     # Return the path to the graph image
#     return graph_path