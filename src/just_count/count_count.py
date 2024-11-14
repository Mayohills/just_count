import just_count.square as square
import click

@click.command()
@click.argument("input", default = 5)

def main(input):
    print(f"The square of {input} is {square.square(input)}")

if __name__ == '__main__':
    main()