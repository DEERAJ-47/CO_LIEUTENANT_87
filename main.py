from tkinter import *

from matplotlib.pyplot import colorbar
from numpy import blackman

root = Tk()
root.geometry("500x500")
root.title("CO_LIEUTANENT-87")
root.config(bg = 'greenyellow')
bg = PhotoImage(file='E:\PROGRAMMING\PYTHON\CO-L-87\\1141.png')

def displayData():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid

    # default source = john_hopkins
    covid = Covid(source='worldometers')
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        for country in country_names:
            cases.append(covid.get_status_by_country_name(country))
            root.update()

        for case in cases:
            confirmed.append(case['confirmed'])
            active.append(case['active'])
            deaths.append(case['deaths'])
            recovered.append(case['recovered'])

        confirmed_patch = mpatches.Patch(color='red', label='Confirmed')
        active_patch = mpatches.Patch(color='blue', label='Active')
        recovered_patch = mpatches.Patch(color='green', label='Recovered')
        deaths_patch = mpatches.Patch(color='black', label='Deaths')

        plt.legend(handles=[confirmed_patch, active_patch, recovered_patch, deaths_patch])
        for country in range(len(country_names)):
            plt.bar(country_names[country], confirmed[country], color="red")
            plt.bar(country_names[country], active[country], color="blue")
            plt.bar(country_names[country], recovered[country], color="green")
            plt.bar(country_names[country], deaths[country], color="black")

        plt.title('Current Covid-19 Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases (in millions)')
        plt.show()
    except Exception as e:
        print(f"Enter correct details country. \n {e}")

Label(root, text="CO_LIEUTANENT-87",font = ('Fixedsys',25,'bold'), bg = 'greenyellow', bd = 20).pack()

Label(root, text="Enter country name: ",font = ('Fixedsys',20,'bold'), bg = 'greenyellow', bd = 20).pack()

data = StringVar()
data.set("")

entry = Entry(root, textvariable=data, width=50,border=20,font = ('Fixedsys',20,'bold'),bg='yellow').pack()
print("\n \n \n")

Button(root, text="\n      Show Data       \n", command=displayData,font = ('Fixedsys',16,'bold')).pack()

root.mainloop()
