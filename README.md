# pulse-fingerprint
A python script to identify the year of the last patch applied on a Pulse Secure appliance based on error pages information leak. It does not rely on *dana-na/nc/nc_gina_ver.txt*, which is sometimes removed to avoid providing too much information.
The biggest limitation of this tool is that it only provides the release date of the last patch applied. The version has to be fetched from Pulse website according to the context.

### Information

The script will perform Pulse detection and identify information disclosure in error pages. Requires Python 3 to run.

### RUN

./pulse_scanner.py http(s)://yourdomain.something

### Example 
![image](https://user-images.githubusercontent.com/39335291/116934446-49841780-ac65-11eb-864c-bfbc6ebec8b3.png)

