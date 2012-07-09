class route:
    def GET(self,render,path):
        print "path is %s ;"%path
        return render.hello()
