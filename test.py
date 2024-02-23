import cvxpy as cp

# Create two scalar optimizatino variables.
# 2つの最適化するスカラーの変数を作成
x = cp.Variable()
y = cp.Variable()

# Create two constraints
# 2つの制約条件の作成
constraints = [x+y==0.5,
               x-y>=1]
# From objective.
# 最小化したい目的関数
obj = cp.Minimize((x-y)**2)

# Form and solve problem.
prob = cp.Problem(obj,constraints)
prob.solve() #Returns the optimal value.　(.solve()で設定した問題を解く)
print("status:",prob.status)
print("optimal value",prob.value)
print("optimal var", x.value,y.value)