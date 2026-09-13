import React from 'react';

export const ClassicalThumbnail: React.FC = () => {
  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: '#f3f2f2',
        color: '#201f1d',
        fontFamily: '"Lora", Georgia, serif',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: '50px 70px',
        boxSizing: 'border-box',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Top Header replicating apps/ui/index.html */}
      <header
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-end',
          paddingBottom: '20px',
          borderBottom: '1px solid rgba(32, 31, 29, 0.16)',
        }}
      >
        <div>
          <div style={{ display: 'flex', alignItems: 'baseline', gap: '16px' }}>
            <h1
              style={{
                fontFamily: '"Cormorant Garamond", Georgia, serif',
                fontSize: '56px',
                fontWeight: 600,
                letterSpacing: '0.04em',
                margin: 0,
                color: '#201f1d',
              }}
            >
              F.R.E.D
            </h1>
            <span
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                fontSize: '12px',
                letterSpacing: '0.14em',
                textTransform: 'uppercase',
                padding: '4px 12px',
                border: '1px solid #b68235',
                color: '#b68235',
                borderRadius: '4px',
                fontWeight: 600,
              }}
            >
              Fraude Detection Engine
            </span>
            <span
              style={{
                fontSize: '11px',
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
                padding: '4px 9px',
                border: '1px solid #8c2f39',
                color: '#8c2f39',
                backgroundColor: 'rgba(140,47,57,0.07)',
                borderRadius: '2px',
                fontWeight: 700,
              }}
            >
              PAUSE ACTIVE
            </span>
          </div>
          <p
            style={{
              margin: '8px 0 0 0',
              fontSize: '18px',
              color: 'rgba(32, 31, 29, 0.65)',
              maxWidth: '65ch',
            }}
          >
            Protección conductual pre-envío contra estafas por coerción y engaño en SPEI.
          </p>
        </div>

        {/* Live Simulator & URL indicator */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '24px' }}>
          <div style={{ paddingLeft: '20px', borderLeft: '1px solid rgba(32, 31, 29, 0.16)', textAlign: 'right' }}>
            <div style={{ fontSize: '11px', letterSpacing: '0.14em', textTransform: 'uppercase', color: '#7d5411', fontWeight: 600 }}>
              Reloj simulado
            </div>
            <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '26px', fontWeight: 600, marginTop: '2px' }}>
              Día 3 de 30 · 11:30 hrs
            </div>
          </div>

          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 16px',
              border: '1px solid rgba(32, 31, 29, 0.2)',
              borderRadius: '4px',
              backgroundColor: '#eae9e9',
            }}
          >
            <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#8c2f39' }} />
            <span style={{ fontSize: '13px', letterSpacing: '0.06em', textTransform: 'uppercase', fontWeight: 600 }}>
              sixsevencitos.tech
            </span>
          </div>
        </div>
      </header>

      {/* Main Content Area: Left Cards + Feed, Right Phone & Signals */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.25fr 0.75fr', gap: '30px', margin: '20px 0', alignItems: 'start' }}>
        
        {/* Left Column: Stat Cards + Live Feed */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Top 2 Stat Cards */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '18px' }}>
            {/* Bank Card */}
            <div
              style={{
                border: '1px solid rgba(32, 31, 29, 0.16)',
                borderRadius: '4px',
                padding: '16px 20px',
                backgroundColor: '#ffffff',
                boxShadow: '0 1px 3px rgba(45, 43, 43, 0.08)',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '8px' }}>
                <span style={{ fontSize: '11px', letterSpacing: '0.1em', textTransform: 'uppercase', color: '#b68235', fontWeight: 600 }}>
                  Métricas de institución bancaria
                </span>
                <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '3px', backgroundColor: '#eae7e7', color: '#444141', textTransform: 'uppercase' }}>
                  API Pública
                </span>
              </div>
              <hr style={{ border: 0, height: '1px', backgroundColor: 'rgba(32, 31, 29, 0.12)', margin: '8px 0 12px 0' }} />
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '12px' }}>
                <div>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>Evaluadas</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '36px', lineHeight: 1.1, fontWeight: 600 }}>615</div>
                </div>
                <div style={{ paddingLeft: '12px', borderLeft: '1px solid rgba(32, 31, 29, 0.16)' }}>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>Intervenciones</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '36px', lineHeight: 1.1, fontWeight: 600, color: '#7d5411' }}>9</div>
                </div>
                <div style={{ paddingLeft: '12px', borderLeft: '1px solid rgba(32, 31, 29, 0.16)' }}>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>Latencia p95</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '36px', lineHeight: 1.1, fontWeight: 600 }}>
                    3.6<span style={{ fontSize: '15px', fontFamily: '"Lora", serif' }}> ms</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Simulation Ground Truth Card */}
            <div
              style={{
                border: '1px solid rgba(32, 31, 29, 0.16)',
                borderRadius: '4px',
                padding: '16px 20px',
                backgroundColor: '#ffffff',
                boxShadow: '0 1px 3px rgba(45, 43, 43, 0.08)',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '8px' }}>
                <span style={{ fontSize: '11px', letterSpacing: '0.1em', textTransform: 'uppercase', color: '#b68235', fontWeight: 600 }}>
                  Verdad de simulación
                </span>
                <span style={{ fontSize: '11px', color: '#2f5d4a', fontWeight: 600 }}>
                  100% Recall
                </span>
              </div>
              <hr style={{ border: 0, height: '1px', backgroundColor: 'rgba(32, 31, 29, 0.12)', margin: '8px 0 12px 0' }} />
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '12px' }}>
                <div>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>APP Interceptados</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '36px', lineHeight: 1.1, fontWeight: 600, color: '#8c2f39' }}>6 / 6</div>
                </div>
                <div style={{ paddingLeft: '12px', borderLeft: '1px solid rgba(32, 31, 29, 0.16)' }}>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>Pesos protegidos</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '28px', lineHeight: 1.1, fontWeight: 600, color: '#2f5d4a' }}>
                    $146,800
                  </div>
                </div>
                <div style={{ paddingLeft: '12px', borderLeft: '1px solid rgba(32, 31, 29, 0.16)' }}>
                  <div style={{ fontSize: '11px', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)', letterSpacing: '0.08em' }}>FP PyME</div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '36px', lineHeight: 1.1, fontWeight: 600, color: '#2f5d4a' }}>
                    0.0<span style={{ fontSize: '15px', fontFamily: '"Lora", serif' }}>%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Feed Table Card */}
          <div
            style={{
              border: '1px solid rgba(32, 31, 29, 0.16)',
              borderRadius: '4px',
              backgroundColor: '#ffffff',
              overflow: 'hidden',
              boxShadow: '0 2px 6px rgba(45, 43, 43, 0.05)',
            }}
          >
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'baseline',
                padding: '12px 18px',
                borderBottom: '1px solid rgba(32, 31, 29, 0.16)',
                backgroundColor: '#eae9e9',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'baseline', gap: '8px' }}>
                <h4 style={{ margin: 0, fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '20px', fontWeight: 600 }}>
                  Feed en tiempo real
                </h4>
                <span style={{ fontSize: '12px', color: 'rgba(32, 31, 29, 0.55)' }}>
                  Evaluaciones continuas SPEI
                </span>
              </div>
              <div style={{ display: 'flex', gap: '14px', fontSize: '11px', letterSpacing: '0.06em', textTransform: 'uppercase' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                  <span style={{ width: '7px', height: '7px', border: '1px solid #2f5d4a', backgroundColor: '#e4ece7' }} /> Allow
                </span>
                <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                  <span style={{ width: '7px', height: '7px', border: '1px solid #7d5411', backgroundColor: '#fff3e4' }} /> Challenge
                </span>
                <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                  <span style={{ width: '7px', height: '7px', border: '1px solid #8c2f39', backgroundColor: '#f4e4e5' }} /> Pause
                </span>
              </div>
            </div>

            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13.5px' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(32, 31, 29, 0.12)', textAlign: 'left', fontSize: '11px', color: 'rgba(32, 31, 29, 0.55)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
                  <th style={{ padding: '8px 16px' }}>Decisión</th>
                  <th style={{ padding: '8px 12px' }}>Origen y destino</th>
                  <th style={{ padding: '8px 12px', textAlign: 'right' }}>Monto</th>
                  <th style={{ padding: '8px 16px', textAlign: 'right' }}>Hora</th>
                </tr>
              </thead>
              <tbody>
                {/* Scam Row Intercepted - Highlighted */}
                <tr style={{ backgroundColor: '#faf1f1', borderLeft: '4px solid #8c2f39', borderBottom: '1px solid rgba(32, 31, 29, 0.12)' }}>
                  <td style={{ padding: '10px 16px' }}>
                    <span style={{ fontSize: '10.5px', letterSpacing: '0.12em', textTransform: 'uppercase', padding: '3px 8px', border: '1px solid #8c2f39', color: '#8c2f39', backgroundColor: 'rgba(140,47,57,0.07)', borderRadius: '2px', fontWeight: 700 }}>
                      PAUSE
                    </span>
                  </td>
                  <td style={{ padding: '10px 12px' }}>
                    <strong>victim_target_004</strong> → 646180157088992112 (STP)
                    <div style={{ fontSize: '11px', color: '#8c2f39', marginTop: '2px' }}>
                      Pausado: llamada activa + beneficiario nuevo &lt; 15m + estructuración
                    </div>
                  </td>
                  <td style={{ padding: '10px 12px', textAlign: 'right', fontWeight: 700, color: '#8c2f39', fontSize: '15px' }}>
                    $12,450.00
                  </td>
                  <td style={{ padding: '10px 16px', textAlign: 'right', color: 'rgba(32, 31, 29, 0.6)' }}>
                    D3 11:30
                  </td>
                </tr>

                {/* Normal Allow Row */}
                <tr style={{ borderBottom: '1px solid rgba(32, 31, 29, 0.12)' }}>
                  <td style={{ padding: '9px 16px' }}>
                    <span style={{ fontSize: '10.5px', letterSpacing: '0.12em', textTransform: 'uppercase', padding: '3px 8px', border: '1px solid #2f5d4a', color: '#2f5d4a', backgroundColor: 'rgba(47,93,74,0.07)', borderRadius: '2px', fontWeight: 700 }}>
                      ALLOW
                    </span>
                  </td>
                  <td style={{ padding: '9px 12px' }}>
                    merchant_pyme_006 → 012180004561899120 (BBVA)
                  </td>
                  <td style={{ padding: '9px 12px', textAlign: 'right', fontWeight: 600 }}>
                    $8,452.22
                  </td>
                  <td style={{ padding: '9px 16px', textAlign: 'right', color: 'rgba(32, 31, 29, 0.6)' }}>
                    D3 10:45
                  </td>
                </tr>

                {/* Normal Allow Row 2 */}
                <tr style={{ borderBottom: '1px solid rgba(32, 31, 29, 0.12)' }}>
                  <td style={{ padding: '9px 16px' }}>
                    <span style={{ fontSize: '10.5px', letterSpacing: '0.12em', textTransform: 'uppercase', padding: '3px 8px', border: '1px solid #2f5d4a', color: '#2f5d4a', backgroundColor: 'rgba(47,93,74,0.07)', borderRadius: '2px', fontWeight: 700 }}>
                      ALLOW
                    </span>
                  </td>
                  <td style={{ padding: '9px 12px' }}>
                    consumer_normal_018 → 002180019283746519 (Banamex)
                  </td>
                  <td style={{ padding: '9px 12px', textAlign: 'right', fontWeight: 600 }}>
                    $1,250.00
                  </td>
                  <td style={{ padding: '9px 16px', textAlign: 'right', color: 'rgba(32, 31, 29, 0.6)' }}>
                    D3 09:12
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* Right Column: Phone Mockup styled exactly like Classical UI */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <div
            style={{
              width: '340px',
              border: '1px solid #bab6b6',
              borderRadius: '24px',
              padding: '12px',
              backgroundColor: '#eae9e9',
              boxShadow: '0 8px 24px rgba(45, 41, 41, 0.14)',
            }}
          >
            <div
              style={{
                border: '1px solid rgba(32, 31, 29, 0.16)',
                borderRadius: '16px',
                backgroundColor: '#f3f2f2',
                overflow: 'hidden',
              }}
            >
              {/* Phone Bar */}
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '10px 16px',
                  borderBottom: '1px solid rgba(32, 31, 29, 0.16)',
                  fontSize: '10px',
                  letterSpacing: '0.12em',
                  textTransform: 'uppercase',
                  fontWeight: 600,
                  color: 'rgba(32, 31, 29, 0.7)',
                }}
              >
                <span>BANCA MÓVIL</span>
                <span>SPEI 24/7</span>
              </div>

              {/* Phone Body */}
              <div style={{ padding: '18px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
                <div>
                  <div style={{ fontSize: '10px', letterSpacing: '0.1em', textTransform: 'uppercase', color: 'rgba(32, 31, 29, 0.55)' }}>
                    Monto propuesto
                  </div>
                  <div style={{ fontFamily: '"Cormorant Garamond", Georgia, serif', fontSize: '32px', fontWeight: 600, marginTop: '2px' }}>
                    $12,450.00 <span style={{ fontSize: '14px', fontFamily: '"Lora", serif' }}>MXN</span>
                  </div>
                </div>

                <div style={{ fontSize: '12px', borderTop: '1px solid rgba(32, 31, 29, 0.12)', paddingTop: '8px' }}>
                  <div style={{ color: 'rgba(32, 31, 29, 0.55)' }}>Destinatario</div>
                  <div style={{ fontFamily: 'monospace', fontSize: '12px', marginTop: '2px' }}>
                    646180157088992112
                  </div>
                  <div style={{ fontSize: '11px', color: '#7d5411', marginTop: '2px' }}>
                    STP · Beneficiario nuevo (&lt; 15m)
                  </div>
                </div>

                {/* Classical Alert Callout */}
                <div
                  style={{
                    backgroundColor: 'rgba(140,47,57,0.08)',
                    border: '1px solid #8c2f39',
                    borderRadius: '4px',
                    padding: '12px',
                  }}
                >
                  <div style={{ color: '#8c2f39', fontSize: '11px', fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: '4px' }}>
                    ⚠️ Pausa de seguridad
                  </div>
                  <div style={{ fontSize: '12px', lineHeight: 1.4, color: '#444141' }}>
                    Pausamos esta transferencia por señales de riesgo durante una llamada telefónica activa. Los bancos nunca piden transferencias por teléfono.
                  </div>
                </div>

                {/* Cancel Button */}
                <button
                  style={{
                    border: '1.5px solid #8c2f39',
                    color: '#ffffff',
                    backgroundColor: '#8c2f39',
                    fontSize: '13px',
                    letterSpacing: '0.04em',
                    padding: '12px',
                    borderRadius: '4px',
                    fontWeight: 600,
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(140,47,57,0.25)',
                  }}
                >
                  ✓ $12,450.00 MXN PROTEGIDOS
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>

      {/* Footer bar */}
      <footer
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderTop: '1px solid rgba(32, 31, 29, 0.16)',
          paddingTop: '16px',
          fontSize: '13px',
          color: 'rgba(32, 31, 29, 0.6)',
        }}
      >
        <div>
          <strong>Capital One HackMTY 2026</strong> · Real-Time Anomaly & Security Sentinel
        </div>
        <div style={{ fontFamily: 'monospace', color: '#b68235', fontWeight: 600 }}>
          https://sixsevencitos.tech/
        </div>
      </footer>
    </div>
  );
};
