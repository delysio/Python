Various files that I have written in Python.

# Python

## Skip_Trackdata

A program that parses *.dsk disk images for the FDD 3000 so that they can be opened seamlessly in the CPM DSK Tool. The processed image has to be cleared from the header (first 256 bytes), followed by 256 bytes of track data, 4 KB of data have to be fetched, 256 bytes of track data have to be skipped, etc.

After truncating the mentioned data, the image can be loaded into CP/M Disk Tool with these parameters without problems.
