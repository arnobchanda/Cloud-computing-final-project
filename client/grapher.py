import matplotlib.pyplot as plt

plt.ion()

class Updater():
    min_x = 0
    max_x = 10
    
    def on_launch(self):
        self.figure, self.ax = plt.subplots()
        self.lines1, = self.ax.plot([],[], 'r-')
        self.lines2, = self.ax.plot([],[], 'g-')
        self.lines3, = self.ax.plot([],[], 'b-')
                            
        self.ax.set_autoscaley_on(True)
        # self.ax.set_xlim(self.min_x, self.max_x)
        
        self.ax.grid()
        
    def on_running(self, xdata, y1data, y2data, y3data):
        self.lines1.set_xdata(xdata)
        self.lines1.set_ydata(y1data)
        self.lines2.set_xdata(xdata)
        self.lines2.set_ydata(y2data)
        self.lines3.set_xdata(xdata)
        self.lines3.set_ydata(y3data)
        
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        
    