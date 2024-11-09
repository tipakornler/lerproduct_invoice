from django.db import models
import datetime

class trans(models.Model):
    send_date = models.DateField(default=datetime.date.today,blank=True, null=False , unique=True, primary_key=True)
    mile_start =  models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True , help_text="ไมล์ก่อนออก")
    mile_stop =  models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, help_text="ไมล์จบงาน")
    toll_fee =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True , help_text="ยอดค่าทางด่วน")
    fuel_cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="ยอดค่าน้ำมัน")
    outsouce_trans =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="ค่าขนส่ง")
    other_cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="ยอดค่าใช้จ่ายอื่นๆ")
    other_cost_remark = models.CharField(max_length=300, null=True, blank=True , help_text="ค่าใช้จ่ายอะไร")
    receive = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="รายได้ค่าขนส่ง")
    other_receive = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="รายได้ค่าขนส่งอื่นๆ")
    remark = models.CharField(max_length=300, null=True, blank=True , help_text="หมายเหตุ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)


    def mile_sum(self):
            return self.mile_stop-self.mile_start if self.mile_start == 0 else ""