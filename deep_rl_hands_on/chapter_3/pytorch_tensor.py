import torch

if __name__ == '__main__':
    v1 = torch.tensor([1.0, 1.0], requires_grad=True)
    v2 = torch.tensor([2.0, 2.0])

    v_sum = v1 + v2
    print(f'v_sum = {v_sum}')

    v_res = (2 * v_sum).sum()
    print(f'v_res = {v_res}')

    v_res.backward()

    print(v1.grad)
