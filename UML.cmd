pyreverse --filter-mode=ALL -o dot .\OOPDraw

start "" dot -T jpg -o OOPDraw.jpg packages.dot
start "" dot -T jpg -o OOPDrawClasses.jpg classes.dot

start "" OOPDrawClasses.jpg

