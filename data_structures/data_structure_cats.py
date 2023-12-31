{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "The following application simply removes calico and persian from the list of big cats. It then places the house cats into their own list.",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "big_cats = ['calico', 'persian', 'lion', 'tiger', 'cheetah', 'leopard', 'bobcat', 'north american mountain lion']\n\n# Iterates through list of big_cats printing out each instance in title format.\nfor cat in big_cats:\n    print(cat.title())\n\n# Adds liger to the list of big_cats.\nif 'liger' not in big_cats:\n    cats.append('liger')\n\n# Creates an empty list for house cats.\nhouse_cats = []\n\n# Iterates through list of big_cats and if it finds a calico cat or persian cat it appends the cat to the house_cat list.\nfor cat in big_cats:\n    if cat == 'calico' or cat == 'persian':\n        house_cats.append(cat)\n\n# Remove 'calico' and 'persian' from the original 'cats' list\nbig_cats = [cat for cat in big_cats if cat not in ['calico', 'persian']]\n\n# Prints out the new lists for big_cats and house_cats.\nprint(\"\\nOriginal cats list:\", big_cats)\nprint(\"House cats list:\", house_cats)\n\nprint(f\"\\n\\tIt is not likely that you will see people with a {cats[0].title()} as a pet.\")\nprint(f\"\\n\\tThat does not mean it doesn't happen though!\")\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "text": "Calico\nPersian\nLion\nTiger\nCheetah\nLeopard\nBobcat\nNorth American Mountain Lion\n\nOriginal cats list: ['lion', 'tiger', 'cheetah', 'leopard', 'bobcat', 'north american mountain lion']\nHouse cats list: ['calico', 'persian']\n\n\tIt is not likely that you will see people with a Lion as a pet.\n\n\tThat does not mean it doesn't happen though!\n",
          "output_type": "stream"
        }
      ],
      "execution_count": 27
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}