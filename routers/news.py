from fastapi import APIRouter

#创建APIRouter实例
#prefix就是路由前缀，tags就是分组标签，方便docs查看
router=APIRouter(prefix="/api/news",tags=['news'])

@router.get("/categories")
async def get_categories():
    return {"msg":"获取分类成功"}