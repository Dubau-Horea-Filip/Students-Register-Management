class Settings:

    def read(self):
        v=[0,0]
        a=0
        f = open("settings.properties", "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(" ")
            v[a]=str(line[2])
            a=a+1
            line = f.readline().strip()
        return  v