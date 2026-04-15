from fastapi import APIRouter
#tags可以属于多个组，所以用列表
router=APIRouter(prefix="/api/user",tags=["user"])

@router.get("/detail_message")
async def get_user_detail_message():
    
    return{"msg":"获取用户详细信息"}