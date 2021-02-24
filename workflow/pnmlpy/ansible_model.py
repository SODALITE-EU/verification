import yaml


class AnsibleTask:
    def __init__(self, name, condition=None, loop=None):
        self.name = name
        self.condition = condition
        self.loop = loop
        # Relationship: "A deck has many cards"


class AnsibleRoleParser:

    def parse(self, file):
        tasks = []
        with open(file) as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            for doc in docs:
                for x in doc:
                    task = AnsibleTask(name=x['name'])
                    if 'when' in x:
                        task.condition = x['when']
                    if 'with_items' in x:
                        task.loop = x['with_items']
                    tasks.append(task)
        return tasks
