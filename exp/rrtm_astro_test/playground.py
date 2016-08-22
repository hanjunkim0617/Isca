import numpy as np
import os

from gfdl.experiment import Experiment, DiagTable

baseexp = Experiment('rrtm_astro_minimal_changes', overwrite_data=True)

#s Define input files for experiment - by default they are found in exp_dir/input/

baseexp.inputfiles = [os.path.join(os.getcwd(),'input/ozone_1990.nc'),os.path.join(os.getcwd(),'input/co2.nc')]

#s Define srcmods - by default they are found in exp_dir/srcmods/

diag = DiagTable()

diag.add_file('atmos_hourly', 1, 'hours', time_units='days')
diag.add_file('atmos_hourly_mk2', 1, 'hours', time_units='days')
diag.add_file('atmos_daily', 1, 'days', time_units='days')
diag.add_file('atmos_daily_mk2', 1, 'days', time_units='days')

# Define diag table entries 
diag.add_field('dynamics', 'ps', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'bk', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'pk', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'vor', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'div', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'ucomp', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'vcomp', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'temp', time_avg=True, files=['atmos_hourly'])
diag.add_field('atmosphere', 'rh', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'slp', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'omega', time_avg=True, files=['atmos_hourly'])
diag.add_field('dynamics', 'height', time_avg=True, files=['atmos_hourly'])


diag.add_field('rrtm_radiation', 'tdt_rad', time_avg=True, files=['atmos_hourly'])
diag.add_field('rrtm_radiation', 'flux_sw', time_avg=True, files=['atmos_hourly'])
diag.add_field('rrtm_radiation', 'flux_lw', time_avg=True, files=['atmos_hourly'])
diag.add_field('rrtm_radiation', 'tdt_sw', time_avg=True, files=['atmos_hourly'])
diag.add_field('rrtm_radiation', 'tdt_lw', time_avg=True, files=['atmos_hourly'])

diag.add_field('rrtm_radiation', 'coszen', time_avg=True, files=['atmos_hourly', 'atmos_daily'])
diag.add_field('rrtm_radiation', 'fracday', time_avg=True, files=['atmos_hourly', 'atmos_daily'])
diag.add_field('rrtm_radiation', 'half_day', time_avg=True, files=['atmos_hourly', 'atmos_daily'])

diag.add_field('rrtm_radiation', 'coszen', time_avg=False, files=['atmos_hourly_mk2','atmos_daily_mk2'])


diag.add_field('dynamics', 'ps', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'bk', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'pk', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'vor', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'div', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'ucomp', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'vcomp', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'temp', time_avg=True, files=['atmos_daily'])
diag.add_field('atmosphere', 'rh', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'slp', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'omega', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'height', time_avg=True, files=['atmos_daily'])
diag.add_field('dynamics', 'height_half', time_avg=True, files=['atmos_daily'])

diag.add_field('mixed_layer', 't_surf', time_avg=True, files=['atmos_daily'])

diag.add_field('atmosphere', 'convection_rain', time_avg=True, files=['atmos_daily'])
diag.add_field('atmosphere', 'condensation_rain', time_avg=True, files=['atmos_daily'])

diag.add_field('rrtm_radiation', 'tdt_rad', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'flux_sw', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'flux_lw', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'tdt_sw', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'tdt_lw', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'co2', time_avg=True, files=['atmos_daily'])
diag.add_field('rrtm_radiation', 'ozone', time_avg=True, files=['atmos_daily'])

diag.add_field('damping', 'udt_rdamp', time_avg=True, files=['atmos_daily'])
diag.add_field('damping', 'vdt_rdamp', time_avg=True, files=['atmos_daily'])
diag.add_field('damping', 'tdt_diss_rdamp', time_avg=True, files=['atmos_daily'])

diag.add_field('vert_turb', 'z_pbl', time_avg=True, files=['atmos_daily'])

diag.add_field('mixed_layer', 'flux_lhe', time_avg=True, files=['atmos_daily'])
diag.add_field('mixed_layer', 'flux_t', time_avg=True, files=['atmos_daily'])
diag.add_field('mixed_layer', 'ml_heat_cap', time_avg=True, files=['atmos_daily'])


baseexp.use_diag_table(diag)

baseexp.compile()

baseexp.clear_rundir()

#s Namelist changes from default values
baseexp.namelist['main_nml'] = {
     'days'   : 1,	
     'hours'  : 0,
     'minutes': 0,
     'seconds': 0,			
     'dt_atmos':720,
     'current_date' : [0001,1,1,0,0,0],
     'calendar' : 'thirty_day'
}


baseexp.namelist['idealized_moist_phys_nml']['two_stream_gray'] = False
baseexp.namelist['idealized_moist_phys_nml']['do_rrtm_radiation'] = True
baseexp.namelist['idealized_moist_phys_nml']['do_bm'] = True
baseexp.namelist['idealized_moist_phys_nml']['lwet_convection'] = False

baseexp.namelist['rrtm_radiation_nml']['do_read_ozone'] = True


baseexp.namelist['mixed_layer_nml']['depth'] = 20.
baseexp.namelist['mixed_layer_nml']['delta_T'] = 0.
baseexp.namelist['mixed_layer_nml']['do_qflux'] = False

baseexp.namelist['qflux_nml']['qflux_amp'] = 0.0


baseexp.namelist['astronomy_nml']['ecc'] = 0.0 #s make orbit circular. 

baseexp.namelist['rrtm_radiation_nml']['solr_cnst'] = 1360. #s set solar constant to 1360, rather than default of 1368.22
baseexp.namelist['rrtm_radiation_nml']['solday'] = 180 #s set solar constant to 1360, rather than default of 1368.22
baseexp.namelist['rrtm_radiation_nml']['dt_rad'] = 3600 #s set solar constant to 1360, rather than default of 1368.22
baseexp.namelist['rrtm_radiation_nml']['do_rad_time_avg'] = True #s set solar constant to 1360, rather than default of 1368.22

#s Using perpetual equinox
#baseexp.namelist['astro_nml']['solday'] = 90.0 
#s End namelist changes from default values


for evap_res in [1]:
    evap_res_name = evap_res
    exp = Experiment('rrtm_minimal_changes_fix_seasonal_coszen_latitude_averaging_%d' % evap_res_name, overwrite_data=True)
    exp.clear_rundir()

    exp.use_diag_table(diag)
    exp.execdir = baseexp.execdir

    exp.inputfiles = baseexp.inputfiles

    exp.namelist = baseexp.namelist.copy()

    exp.runmonth(1, use_restart=False, num_cores=4)

