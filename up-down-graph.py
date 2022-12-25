import matplotlib.pyplot as plt
import psutil

# Initialize variables to track the total amount of data uploaded and downloaded
uploaded_data = 0
downloaded_data = 0

# Set the number of data points to collect (e.g. every 5 seconds)
data_points = 60

# Initialize empty lists to store the data points
upload_data_points = []
download_data_points = []

# Collect data for the specified number of data points
for i in range(data_points):
  # Get the network statistics using the psutil library
  net_stats = psutil.net_io_counters()
  
  # Calculate the amount of data uploaded and downloaded since the last data point
  uploaded = net_stats.bytes_sent - uploaded_data
  downloaded = net_stats.bytes_recv - downloaded_data
  
  # Add the data to the lists of data points
  upload_data_points.append(uploaded)
  download_data_points.append(downloaded)
  
  # Update the total amount of data uploaded and downloaded
  uploaded_data = net_stats.bytes_sent
  downloaded_data = net_stats.bytes_recv
  
  # Wait 5 seconds before collecting the next data point
  time.sleep(5)

# Create a bar chart to display the data
plt.bar(range(data_points), upload_data_points, label="Upload")
plt.bar(range(data_points), download_data_points, bottom=upload_data_points, label="Download")
plt.legend()
plt.show()