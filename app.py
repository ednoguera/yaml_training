import yaml

if __name__ == '__main__':
    stream = open("test.yaml", "r")
    dic = yaml.safe_load(stream)

    print("SOFTWARE BASE INFO: ")
    for key, value in dic.items():
        print("{}: {} ".format(
            key, str(value)
        ))
