
# User identification

name = input("What's your name? \n")

if name == "Antti" or name == "antti":

        print("Hi there,", name)

else:
        print("Well I'm not sure you should be running this super secret program. Try again, maybe? \n")
        name = input("What's your name? \n")      
        if name == "Antti" or name == "antti":
                print("Now that sounds more like it. Hi there,", name, "!\n")


#Manflu status

manflu = input("I heard you caught a tough case of the manflu :( Is that true? y/n \n")

if manflu == "y":

                print("You poor thing! Here's a little something to cheer you up." )

                import webbrowser

                webbrowser.open_new_tab('https://youtu.be/9sxMr4IdXaU')

                print("Feel better already? Hoping so!")

elif manflu == "n":
                print("Well that's good to hear! Let's celebrate with some kittens.")

                import webbrowser

                webbrowser.open_new_tab('https://youtu.be/9sxMr4IdXaU')

                print("Hope you liked it!")

else:
                print("Hmm, didn't quite catch that.. well, here's some kittens for you in any case!")

                import webbrowser

                webbrowser.open_new_tab('https://youtu.be/9sxMr4IdXaU')

                print("Now how about that.")


