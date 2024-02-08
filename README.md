# LogParser
This Python script analyzes VPC flow logs to extract and list all IP addresses from entries marked as “REJECT”. It also saves each line of rejected traffic into a separate txt file for further analysis.

Features

	•	Extracts all source and destination IP addresses from rejected traffic entries in a VPC flow log.
	•	Outputs a list of unique rejected IP addresses to the console.
	•	Saves detailed entries of rejected traffic to a .txt file for record-keeping and further examination.

Prerequisites

Before you run this script, you need:

	•	Python 3.x installed on your system.
	•	Access to VPC flow log files in .log format that you wish to analyze.

Setup

	1.	Clone or download this repository to your local machine.
	2.	Ensure your VPC flow log file is accessible on your system. Place the log file in the same directory as the script for simplicity, or be ready to specify the full path to the file when running the script.

Usage

To run the script, open a terminal or command prompt, navigate to the directory containing the script, and execute:

python logparser.py path/to/your_log_file.log

Replace path/to/your_log_file.log with the actual path to your VPC flow log file. If the log file is in the same directory as the script, you can simply specify the filename:

python logparser.py your_log_file.log

Output

	•	The script prints a list of unique rejected IP addresses to the console.
	•	A file named rejected_traffic.txt containing the detailed entries of rejected traffic will be created in the script’s directory.

Customization

If your log file uses a different format or delimiter, you may need to modify the script to correctly parse your logs. This primarily involves adjusting the parse_vpc_flow_logs function in the script to match your log file’s specific structure.

Troubleshooting

	•	Script can’t find the log file: Ensure you’ve specified the correct path to your log file. If it’s in a different directory from the script, you need to provide the full path.
	•	Errors while running the script: Make sure you have Python 3.x installed and are using the correct command (python or python3 depending on your system’s configuration).

Contributing

Contributions to improve the script are welcome. Please feel free to fork the repository, make your improvements, and submit a pull request.

Note:

	•	Filename and Paths: Adjust the script name (logparser.py) and example paths as necessary to match your project’s files and structure.


License 

Distributed under the MIT License. 

Contact

Anna Booker 
https://github.com/annabook21/LogParser/
 
