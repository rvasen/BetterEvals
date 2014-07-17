from bs4 import BeautifulSoup

def htmlParse(daEval):
	class Eval:
		def __init__(self,number,department,className,teachers,term,score,units,hours,eligible,respond,url):
			self.number = number
			self.className = className
			self.teachers = teachers
			self.term = term
			self.score = score
			self.units = units
			self.hours = hours
			self.eligible = eligible
			self.respond = respond
			self.url = url

	parsedEval = Eval(number, className, teachers, term, score, units, hours, eligible, respond, url)
	return parsedEval