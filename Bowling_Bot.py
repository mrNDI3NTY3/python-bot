import pyautogui
import time
from rich.console import Console
con = Console()
def timer():
	for i in range(3):
		con.print(f'[bold yellow] TIMER: [bold yellow] {i+1}')
		time.sleep(1)

def checker():
	cords = pyautogui.locateOnScreen('bot_file/accept.png')
	if cords == None:
		return None
	else:
		cords = pyautogui.locateOnScreen('bot_file/accept.png')
		point_cords = pyautogui.center(cords)
		point_cords_x, point_cords_y = point_cords
		con.log("[bold green]Accept button detect! [/bold green]")
		pyautogui.click(point_cords_x, point_cords_y)
		time.sleep(2)

con.print("[bold green]BOWLING BOT[/bold green] [bold]for[/bold] [bold red]ZIPTO[/bold red] [bold cyan]v1.1 indev[bold cyan]")
con.input("[bold cyan]Press enter, please :) [/bold cyan]")
timer()

ball_x, ball_y = pyautogui.position()
con.print(f'[bold cyan]cords balls {ball_x} : {ball_y}[/bold cyan]')
con.input("[bold cyan]Press enter, again :) [/bold cyan]")
timer()

bowling_x, bowling_y = pyautogui.position()
con.print(f'[bold cyan]cords bowling {bowling_x} : {bowling_y}[/bold cyan]')
cycle = int(con.input("[bold cyan]Press enter cycle value: [/bold cyan]"))
timer()

con.rule("[bold green]Start")
for i in range(cycle):
	checker()
	pyautogui.click(ball_x, ball_y)
	time.sleep(4)
	pyautogui.click(bowling_x, bowling_y)
	checker()
	time.sleep(17)
	checker()
	con.log(f'Bowling {i+1}')

pyautogui.alert('stop!')