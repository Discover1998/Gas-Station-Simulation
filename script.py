import random, simpy

run_time = 25
no_of_users = 30
random.seed(42)

collecting_data_to_fill = dict()

class User:
    def __init__(self, user_no, state=None):
        self.user_no = user_no
        self.state = random.choice([True, False]) if state is None else state

class GasFiller:
    def __init__(self, env, n_pumps, n_shop):
        self.env = env
        self.pumps = simpy.Resource(env, capacity=n_pumps)
        self.shop  = simpy.Resource(env, capacity=n_shop)

    def visit_shop(self, user, duration=1):
        with self.shop.request() as req:
            yield req
            yield self.env.timeout(duration)

    def fuel(self, user, duration):
        with self.pumps.request() as req:
            yield req
            yield self.env.timeout(duration)

def user_process(env, station: GasFiller, user: User, arrival_delay=0):
    yield env.timeout(arrival_delay)
    arrive_at = env.now
    print(f"{env.now:>5}  User {user.user_no} arrives (state={user.state})")

    if not user.state:
        yield from station.visit_shop(user, duration=1)
        user.state = True

    t_fill = random.choice([2, 3])
    yield from station.fuel(user, duration=t_fill)

    total = env.now - arrive_at
    collecting_data_to_fill[user.user_no] = total
    print(f"{env.now:>5}  User {user.user_no} departs, total time={total}")

def main():
    env = simpy.Environment()
    station = GasFiller(env, n_pumps=2, n_shop=1)

    for i in range(1, no_of_users + 1):
        u = User(i)
        delay = random.uniform(0, 10)
        env.process(user_process(env, station, u, arrival_delay= delay))

    env.run(until=run_time)

    if collecting_data_to_fill:
        avg_time = sum(collecting_data_to_fill.values()) / len(collecting_data_to_fill)
        print("\nSummary:")
        print(f"  Users served: {len(collecting_data_to_fill)}")
        print(f"  Avg total time in system: {avg_time:.2f}")

if __name__ == "__main__":
    main()
