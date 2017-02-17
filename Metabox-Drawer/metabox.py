from os import path
from mv import fd_types, utils, unit


PART = path.join(path.dirname(__file__),"Metabox","Part with Edgebanding.blend")
DRAWER_RAILS = path.join(path.dirname(__file__),"Metabox","Drawer Rails.blend") 
DRAWER_SIDES = path.join(path.dirname(__file__),"Metabox","Drawer Sides.blend") 
FRONT_FITTINGS = path.join(path.dirname(__file__),"Metabox","Front Fittings.blend") 

 


class PRODUCT_Metabox(fd_types.Assembly):   
    
    library_name = "Metabox"  
    category_name = "Products"   
    
    width = unit.inch(18)
    height = unit.inch(3.375)
    depth = unit.inch(-21.625)
    
   
    
    def draw(self):
        self.create_assembly()
#----------PRODUCT SPECIAL SIZING INFO        
        self.add_tab("Metabox Options", tab_type='HIDDEN')     
        self.add_prompt(name='Side Offset',prompt_type='DISTANCE',value=unit.inch(1.13),tab_index=0) 
        self.add_prompt(name='Bottom Y Offset',prompt_type='DISTANCE',value=unit.inch(1.055),tab_index=0)
        self.add_prompt(name='Back Z Offset',prompt_type='DISTANCE',value=unit.inch(0.225),tab_index=0)
        self.add_prompt(name='Back Y_Loc Offset',prompt_type='DISTANCE',value=unit.inch(.055),tab_index=0)
        self.add_prompt(name='Sidewall Offset',prompt_type='DISTANCE',value=unit.inch(.15),tab_index=0)
        self.add_prompt(name='Front Fittings x Offset',prompt_type='DISTANCE',value=unit.inch(.51),tab_index=0)
        self.add_prompt(name='Front Fittings z Offset',prompt_type='DISTANCE',value=unit.inch(.40),tab_index=0)
        self.add_prompt(name='Model H',prompt_type='DISTANCE',value=unit.inch(5.875),tab_index=0)
        self.add_prompt(name='Model K',prompt_type='DISTANCE',value=unit.inch(4.625),tab_index=0)
        self.add_prompt(name='Model M',prompt_type='DISTANCE',value=unit.inch(3.375),tab_index=0)
        self.add_prompt(name='Model N',prompt_type='DISTANCE',value=unit.inch(2.125),tab_index=0)
        self.add_prompt(name='Model 550',prompt_type='DISTANCE',value=unit.inch(21.625),tab_index=0)
        self.add_prompt(name='Model 500',prompt_type='DISTANCE',value=unit.inch(19.6875),tab_index=0)
        self.add_prompt(name='Model 450',prompt_type='DISTANCE',value=unit.inch(17.6875),tab_index=0)
        self.add_prompt(name='Model 400',prompt_type='DISTANCE',value=unit.inch(15.75),tab_index=0)
        self.add_prompt(name='Model 350',prompt_type='DISTANCE',value=unit.inch(13.75),tab_index=0)
        self.add_prompt(name='Model 270',prompt_type='DISTANCE',value=unit.inch(10.625),tab_index=0)
        
        
        
#--------------SIZING VARIABLES        
        dim_x = self.get_var('dim_x')
        dim_y = self.get_var('dim_y')
        dim_z = self.get_var('dim_z')        
        SO = self.get_var('Side Offset','SO')
        BYO = self.get_var('Bottom Y Offset','BYO')
        BZO = self.get_var('Back Z Offset','BZO')
        BLO = self.get_var('Back Y_Loc Offset','BLO')
        SWO = self.get_var('Sidewall Offset','SWO')
        FXO = self.get_var('Front Fittings x Offset','FXO')
        FZO = self.get_var('Front Fittings z Offset','FZO')
        H = self.get_var('Model H','H')
        K = self.get_var('Model K','K')
        M = self.get_var('Model M','M')
        N = self.get_var('Model N','N')
        M550 = self.get_var('Model 550','M550')
        M500 = self.get_var('Model 500','M500')
        M450 = self.get_var('Model 450','M450')
        M400 = self.get_var('Model 400','M400')
        M350 = self.get_var('Model 350','M350')
        M270 = self.get_var('Model 270','M270')
        
#-----------PRODUCT PARTS                
        drawer_bottom = self.add_assembly(PART)
        drawer_bottom.set_name("Drawer Bottom")
        drawer_bottom.x_dim('dim_x-SO', [dim_x,SO])
        drawer_bottom.y_dim('IF(dim_y>=M550,M550,IF(dim_y>=M500,M500,IF(dim_y>=M450,M450,IF(dim_y>=M400,M400,IF(dim_y>=M350,M350,IF(dim_y>=M270,M270,M270))))))-BYO', [dim_y,M550,M500,M450,M400,M350,M270,BYO])
        drawer_bottom.z_dim(value=unit.inch(.75))
        drawer_bottom.x_loc(value=unit.inch(.59))
        drawer_bottom.y_loc(value=unit.inch(.25))
        drawer_bottom.z_loc(value=unit.inch(.084))
        
        
        drawer_back = self.add_assembly(PART)
        drawer_back.set_name("Drawer Back")
        drawer_back.x_dim('dim_x-SO',[dim_x,SO])
        drawer_back.y_dim('IF(dim_z>=H,H,IF(dim_z>=K,K,IF(dim_z>=M,M,IF(dim_z>=N,N,N))))-BZO', [dim_z,H,K,M,N,BZO])
        drawer_back.z_dim(value=unit.inch(.75))
        drawer_back.x_loc(value=unit.inch(.59))
        drawer_back.y_loc('IF(dim_y>=M550,M550,IF(dim_y>=M500,M500,IF(dim_y>=M450,M450,IF(dim_y>=M400,M400,IF(dim_y>=M350,M350,IF(dim_y>=M270,M270,M270))))))-BLO', [dim_y,BLO,M550,M500,M450,M400,M350,M270])
        drawer_back.z_loc(value=unit.inch(.11))
        drawer_back.x_rot(value=(90))
        
        drawer_rails = self.add_assembly(DRAWER_RAILS)
        drawer_rails.x_dim('dim_x',[dim_x])
        drawer_rails.y_dim('IF(dim_y>=M550,M550,IF(dim_y>=M500,M500,IF(dim_y>=M450,M450,IF(dim_y>=M400,M400,IF(dim_y>=M350,M350,IF(dim_y>=M270,M270,M270))))))', [dim_y,M550,M500,M450,M400,M350,M270])
        drawer_rails.z_dim('IF(dim_z>=H,H,IF(dim_z>=K,K,IF(dim_z>=M,M,IF(dim_z>=N,N,N))))', [dim_z,H,K,M,N])
        drawer_rails.z_loc(value=unit.inch(.32))
        
        drawer_sides = self.add_assembly(DRAWER_SIDES)
        drawer_sides.x_dim('dim_x-SWO',[dim_x,SWO])
        drawer_sides.y_dim('IF(dim_y>=M550,M550,IF(dim_y>=M500,M500,IF(dim_y>=M450,M450,IF(dim_y>=M400,M400,IF(dim_y>=M350,M350,IF(dim_y>=M270,M270,M270))))))', [dim_y,M550,M500,M450,M400,M350,M270])
        drawer_sides.z_dim('IF(dim_z>=H,H,IF(dim_z>=K,K,IF(dim_z>=M,M,IF(dim_z>=N,N,N))))', [dim_z,H,K,M,N])
        
        front_fittings = self.add_assembly(FRONT_FITTINGS)
        front_fittings.x_dim('dim_x-FXO',[dim_x,FXO])
        front_fittings.y_dim('dim_y',[dim_y])
        front_fittings.z_dim('IF(dim_z>=H,H,IF(dim_z>=K,K,IF(dim_z>=M,M,IF(dim_z>=N,N,N))))-FZO', [dim_z,H,K,M,N,FZO])
        
        
        
        
        
        
        
        self.update()                                                                                                                                                                               